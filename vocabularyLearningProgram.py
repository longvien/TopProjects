import random

class Main():
    def __init__(self, langue1, langue2):
        self.l1 = langue1
        self.l2 = langue2
class Insert(Main):
    def __init__(self, langue1, langue2):
        super().__init__(langue1, langue2)
        self.vocab = {}
    def VocabNum(self):
        try:
            vocab_num = int(input('Please enter the number of Vocabulary\n'))
            for i in range(vocab_num):
                l1Input = input(f'Please enter the {self.l1} word:\n') 
                print(f" === Program saved word '{l1Input}' === ")
                l2Input = input(f'Please enter the {self.l2} word:\n') 
                print(f" === Program saved word '{l2Input}' === ")
                print('--------------------------------------------------')
                self.vocab[l1Input] = l2Input
                self.vocab[l2Input] = l1Input
        except:
            raise ValueError('Please enter a valid number!')
            
            
class Learn(Insert):
    def __init__(self, langue1, langue2):
        super().__init__(langue1, langue2)
    def learn(self):
        super().VocabNum()
        while True: 
            entry = random.choice(list(self.vocab.items()))
            ask = random.choice(entry)
            user_input = input(f"Please enter the meaning of {ask}\n")
            if user_input == self.vocab[ask]:
                print('Correct!')
            else:
                print(f'Incorrect! {ask} means {self.vocab[ask]}')
            confirm = input('Next question (y/n)?\n')
            if confirm !=  'y':
                print('=====================================================')
                print('         Thanks for using our programm!              ')
                print('=====================================================')
                break

# Main Program
def main():
    l1 = input('Please enter the first language\n')
    print('--------------------------------------------------')
    l2 = input('Please enter the second language\n')
    print('--------------------------------------------------')
    translator = Learn(l1, l2)
    translator.learn()
main()

#Author: Long Vien