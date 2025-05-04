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
    - Build and run the STORM pipeline entirely in-memory (no file output).
    """

    def __init__(self):
        """Initialize the pipeline manager and prepare language model configurations."""
        self.lm_configs = STORMWikiLMConfigs()  # Holds LM configurations for different STORM components
        self._setup_models()

    def _setup_models(self) -> None:
        """
        Set up and assign language models to each stage of the STORM pipeline.
        Uses OpenAI models via Litellm with temperature/top_p settings to control creativity.
        """

        # Configure a lightweight model for simulations and question generation
        gpt_35 = LitellmModel(
            model='gpt-3.5-turbo',
            max_tokens=500,
            api_key=settings.openai_api_key,
            temperature=1.0,
            top_p=0.9,
        )

        # Configure a more capable model for outline generation and article writing
        gpt_4 = LitellmModel(
            model='gpt-4o',
            max_tokens=3000,
            api_key=settings.openai_api_key,
            temperature=1.0,
            top_p=0.9,
        )

        # Assign LMs to respective STORM components
        self.lm_configs.set_conv_simulator_lm(gpt_35)
        self.lm_configs.set_question_asker_lm(gpt_35)
        self.lm_configs.set_outline_gen_lm(gpt_4)
        self.lm_configs.set_article_gen_lm(gpt_4)
        self.lm_configs.set_article_polish_lm(gpt_4)

    def run_pipeline(self, topic: str) -> dict:
        """
        Execute the end-to-end STORM pipeline: research → outline → generate article → polish.

        Args:
            topic (str): The topic on which to perform knowledge synthesis.

        Returns:
            dict: Contains the final generated article and structured outline summary.
        """

        # Setup arguments with output_dir=None to avoid writing files
        args = STORMWikiRunnerArguments(output_dir=None)

        # Initialize retrieval mechanism using You.com API
        rm = YouRM(ydc_api_key=settings.ydc_api_key, k=args.search_top_k)

        # Instantiate the runner with configured arguments, models, and retriever
        runner = STORMWikiRunner(args, self.lm_configs, rm)

        # Execute all steps of the STORM pipeline
        runner.run(
            topic=topic,
            do_research=True,
            do_generate_outline=True,
            do_generate_article=True,
            do_polish_article=True,
        )
        runner.post_run()

        return runner.summary()


# Create a global instance of the pipeline manager to be reused across API calls
storm_pipeline_manager = STORMPipelineManager()
