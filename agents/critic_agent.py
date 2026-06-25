class CriticAgent:

    def run(self, analysis):

        return {
            "technical_limitations":
                analysis["technical_limitations"],

            "experimental_limitations":
                analysis["experimental_limitations"]
        }