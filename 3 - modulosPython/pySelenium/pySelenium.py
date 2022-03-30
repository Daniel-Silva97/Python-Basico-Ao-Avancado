from selenium import webdriver
from time import sleep


# Criando a classe para gerenciar as funções
class ChromeAuto:
    def __init__(self):
        self.driverPath = r'CAMINHO_CHROME_DRIVER'
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driverPath,
            # options=self.options
        )

    # Abrindo o chrome
    def acessa(self, site):
        self.chrome.get(site)

    # Clicando no botão de login
    def clicaSignIn(self):
        try:
            botaoSignIn = self.chrome.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
            botaoSignIn.click()
        except Exception as e:
            print('Erro ao clicar Sign-In:', e)

    # Digitando Usuário e senha
    def efetuarLogin(self):
        # Inserindo o usuário
        try:
            inputUser = self.chrome.find_element_by_id('login_field')
            inputPassword = self.chrome.find_element_by_id('password')
            btnSignUp = self.chrome.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')

            inputUser.send_keys('SEU_USUARIO')
            inputPassword.send_keys('SUA_SENHA')
            sleep(2)
            btnSignUp.click()
        except Exception as e:
            print('Erro ao efetuar login:', e)

    # Clica no botão perfil depois de logado
    def clicarPerfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > '
                'div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no Perfil:', e)

    # Verifica se o nome de perfil está certo
    def verificaNome(self, usuario):
        profile_link = self.chrome.find_element_by_css_selector(
            'body > div.position-relative.js-header-wrapper > header > '
            'div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > '
            'div.header-nav-current-user.css-truncate > a')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    # Clica no botão de logout
    def clicaSignOut(self):
        try:
            sair = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header '
                                                            '> '
                                                            'div.Header-item.position-relative.mr-0.d-none.d-md-flex '
                                                            '> details > details-menu > form > button')
            sair.click()
        except Exception as e:
            print('Erro ao clicar Sign Out:', e)

    # Fecha o navegador
    def fecharChrome(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    sleep(2)
    chrome.clicaSignIn()
    sleep(2)
    chrome.efetuarLogin()
    sleep(2)
    chrome.clicarPerfil()
    sleep(2)
    chrome.clicaSignOut()
    sleep(2)
    chrome.clicaSignIn()
    sleep(2)
    chrome.efetuarLogin()
    sleep(2)
    chrome.clicarPerfil()
    sleep(2)
    chrome.verificaNome('USUARIO_A_VALIDAR')
    sleep(2)
    chrome.fecharChrome()
