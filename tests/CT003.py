from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def cadastrar_aluno():
    # Configuração do WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Passo 1: Acessar a página principal do sistema
        driver.get("http://sga.leiteviana.com:8080/")  # Substitua pelo URL real da página

        # Passo 2: Informe o nome do usuário
        username_field = driver.find_element(By.ID, "user")
        username_field.send_keys("ocelot")  # Substitua pelo usuário válido

        # Passo 3: Informe a senha do usuário
        password_field = driver.find_element(By.ID, "senha")
        password_field.send_keys("Oi@12345")  # Substitua pela senha válida

        # Passo 4: Clicar no botão de Login
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        login_button.click()

        # Aguarda o redirecionamento para a página principal
        time.sleep(5)

        # Passo 5: Acessar o módulo "Cadastrar Aluno"
        campo_cadastrar_aluno = driver.find_element(By.XPATH, "//a[contains(text(), 'CADASTRAR ALUNO')]")
        campo_cadastrar_aluno.click()

        # Passo 6: Preencher o formulário de cadastro
        time.sleep(2)

        campo_nome = driver.find_element(By.ID, "nome")
        campo_nome.send_keys("José Neto")

        campo_curso = Select(driver.find_element(By.ID, "curso"))
        campo_curso.select_by_visible_text('INFORMATICA')

        campo_gerar_mat = driver.find_element(By.CLASS_NAME, "btn-primary")
        campo_gerar_mat.click()

        time.sleep(1)

        campo_turno = Select(driver.find_element(By.ID, "turno"))
        campo_turno.select_by_visible_text('MATUTINO')

        campo_status = Select(driver.find_element(By.ID, "status"))
        campo_status.select_by_visible_text('INATIVO')

        btn_cadastrar = driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]")
        btn_cadastrar.click()

        # Aguardar e verificar se o cadastro foi realizado
        time.sleep(2)

        #print("Teste CT003 – Sucesso: Cadastro concluído com sucesso.")

    except Exception as e:
        print(f"Erro durante o teste: {e}")
    finally:
        # Fecha o navegador
        driver.quit()

# Executa o teste
cadastrar_aluno()
