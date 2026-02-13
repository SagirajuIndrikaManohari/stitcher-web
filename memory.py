class MemoryManager:
    def __init__(self):
        self.core_context = {
            "project_title": "Reducing Marine Pollution in Tuticorin",
            "rules": [
                "Follow academic ethics",
                "Use verified sources",
                "Focus on environmental sustainability"
            ]
        }

        self.project_state = {
            "current_stage": "Stage 10/36 – Pollution Source Identification",
            "completed_stages": [
                "Problem Definition",
                "Literature Review"
            ],
            "current_focus": "Industrial and port-based pollution"
        }

        self.episodic_memory = []
        self.interaction_count = 0

    def add_interaction(self, text):
        self.episodic_memory.append(text)
        self.interaction_count += 1

    def reset_episodic(self, summary):
        self.episodic_memory = [summary]
