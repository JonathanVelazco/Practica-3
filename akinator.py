class Question:
    def __init__(self, text, yes=None, no=None):
        self.text = text
        self.yes = yes
        self.no = no


class Akinator:
    def __init__(self):
        self.root = Question("¿Es un animal?")

    def play(self):
        current_question = self.root
        while True:
            answer = input(current_question.text + " (s/n): ").lower()
            if answer == 's':
                if current_question.yes:
                    current_question = current_question.yes
                else:
                    print("¡He adivinado!")
                    break
            elif answer == 'n':
                if current_question.no:
                    current_question = current_question.no
                else:
                    self.learn(current_question)
                    break
            else:
                print("Respuesta no válida. Por favor, responde 's' o 'n'.")

    def learn(self, current_question):
        guess = input("No he adivinado. ¿Qué animal era?: ")
        new_question_text = input(f"¿Qué pregunta harías para distinguir un(a) {guess} de un(a) {current_question.text}?: ")
        answer = input(f"Para un(a) {guess}, ¿la respuesta sería 's' o 'n'?: ").lower()

        new_question = Question(new_question_text)
        new_guess = Question(guess)

        if answer == 's':
            new_question.yes = new_guess
            new_question.no = current_question
        else:
            new_question.yes = current_question
            new_question.no = new_guess

        parent_question = self.find_parent(self.root, current_question)
        if parent_question.yes == current_question:
            parent_question.yes = new_question
        else:
            parent_question.no = new_question

    def find_parent(self, node, child):
        if node.yes == child or node.no == child:
            return node
        if node.yes:
            parent = self.find_parent(node.yes, child)
            if parent:
                return parent
        if node.no:
            parent = self.find_parent(node.no, child)
            if parent:
                return parent
        return None


if __name__ == "__main__":
    akinator = Akinator()
    akinator.play()
s
