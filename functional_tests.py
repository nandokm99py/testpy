from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#browser = webdriver.Firefox()

#browser.get('http://localhost:8000')

#assert 'To-Do' in browser.title
#assert 'Django' in browser.title


#pause



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
    
        #browser = webdriver.Firefox()

        #Usuário ouviu falar de um novo site interessante e foi checar
        self.browser.get('http://localhost:8000')

        #Verifica no título e no cabeçalho que é uma lista de coisas a fazer
        #assert 'to-do' in browser.title, "Browser title was " + browser.title
        self.assertIn('To-Do', self.browser.title)
        #self.assertIn('Django', self.browser.title)
       # header_text= self.browser.find_element_by_tag_name('h1').text
       # self.assertIn('To-Do', header_text)
        #self.assertIn('worked', header_text)



        #Ainda há uma caixa de texto esperando para adicionar outro item. Ele
        #digita "Verificar se a quantidade de parafusos é suficiente"

        self.fail('Finish the test!')


       
#É convidado a inserir um item agora mesmo
if __name__ == '__main__':
    unittest.main(warnings='ignore')
        

#Escreve "Comprar parafusos" em uma caixa de texto

#Ao teclar ENTER a página atualiza e agora aparece
# "1 - Comprar parafusos" como item na lista de coisas a fazer

#Ainda há uma caixa de texto convidando a inserir mais itens. Ele coloca "Comprar lâmpadas"

#A página atualiza novamente e agora apresenta os dois itens na lista

#O usuário não sabe se o site vai gravar a lista, então percebe que ele gerou um URL específico
#para ele (há um texto explicativo sobre isso)

#Ele acessa o URL e verifica que a lista está lá

#Satisfeito, volta a dormir

#self.browser.quit()



