from memory import MemoryManager
from geospatial import GeospatialInjector
from summarizer import Summarizer


class Stitcher:
    def __init__(self, token_limit=500):
        self.memory = MemoryManager()
        self.geo = GeospatialInjector()
        self.summarizer = Summarizer()
        self.token_limit = token_limit

    def estimate_tokens(self, text):
        return len(text.split())

    def should_summarize(self):
        episodic_text = " ".join(self.memory.episodic_memory)
        return (
            self.memory.interaction_count >= 5 or
            self.estimate_tokens(episodic_text) >= self.token_limit
        )

    def build_prompt(self, user_query, student_location):
        self.memory.add_interaction(user_query)

        if self.should_summarize():
            summary = self.summarizer.summarize(
                self.memory.episodic_memory
            )
            self.memory.reset_episodic(summary)

        prompt = f"""
You are an environmental research assistant.

PROJECT:
{self.memory.core_context['project_title']}

CORE RULES:
- {" | ".join(self.memory.core_context['rules'])}

PROJECT STATUS:
- {self.memory.project_state['current_stage']}
- Completed: {", ".join(self.memory.project_state['completed_stages'])}
- Focus: {self.memory.project_state['current_focus']}

REGIONAL CONTEXT:
{self.geo.get_context(student_location)}

RECENT CONTEXT:
{" ".join(self.memory.episodic_memory)}

USER QUESTION:
{user_query}

Respond in a clear, academic, and structured manner.
"""
        return prompt.strip()
