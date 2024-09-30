class AnonymousSurvey:
    """Collect anonymous answer to a survay questaion"""
    def __init__(self, question):
        """Store a question, and prepare to store response."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Show all responses that have been given"""
        print("Survey result:")
        for response in self.responses:
            print(f"-{response}")

