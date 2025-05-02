from knowledge_storm import (
    STORMWikiRunnerArguments,
    STORMWikiRunner,
    STORMWikiLMConfigs
)
from knowledge_storm.lm import LitellmModel
from knowledge_storm.rm import YouRM
from config.settings import settings


class STORMPipelineManager:
    """
    Orchestrates the setup and execution of the Stanford STORM knowledge synthesis pipeline.

    Responsibilities:
    - Configure LM (language model) roles using API keys and model settings.
    - Build and run the STORM pipeline in-memory.
    - Avoids writing to disk by default.
    """

    def __init__(self):
        """Initialize and configure LLMs using environment settings."""
        self.lm_configs = STORMWikiLMConfigs()
        self._setup_models()

    def _setup_models(self) -> None:
        """
        Sets up Litellm model configurations for each STORM component.
        """
        gpt_35 = LitellmModel(
            model='gpt-3.5-turbo',
            max_tokens=500,
            api_key=settings.openai_api_key,
            temperature=1.0,
            top_p=0.9,
        )

        gpt_4 = LitellmModel(
            model='gpt-4o',
            max_tokens=3000,
            api_key=settings.openai_api_key,
            temperature=1.0,
            top_p=0.9,
        )

        # Assign models to the STORM LM configs
        self.lm_configs.set_conv_simulator_lm(gpt_35)
        self.lm_configs.set_question_asker_lm(gpt_35)
        self.lm_configs.set_outline_gen_lm(gpt_4)
        self.lm_configs.set_article_gen_lm(gpt_4)
        self.lm_configs.set_article_polish_lm(gpt_4)

    def run_pipeline(self, topic: str) -> dict:
        """
        Execute the full STORM pipeline: retrieval → outline → article → polish.

        Args:
            topic (str): Input topic string to generate structured content.

        Returns:
            dict: Summary of the generated article and outline.
        """
        args = STORMWikiRunnerArguments(output_dir=None)  # No file writing
        rm = YouRM(ydc_api_key=settings.ydc_api_key, k=args.search_top_k)

        runner = STORMWikiRunner(args, self.lm_configs, rm)

        runner.run(
            topic=topic,
            do_research=True,
            do_generate_outline=True,
            do_generate_article=True,
            do_polish_article=True,
        )
        runner.post_run()

        return runner.summary()


storm_pipeline_manager = STORMPipelineManager()