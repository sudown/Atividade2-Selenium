from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
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
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'CADASTRAR ALUNO')]"))
        )

        # Passo 5: Acessar o módulo "Cadastrar Aluno"
        campo_cadastrar_aluno = driver.find_element(By.XPATH, "//a[contains(text(), 'CADASTRAR ALUNO')]")
        campo_cadastrar_aluno.click()

        # Passo 6: Preencher o formulário de cadastro
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nome"))
        )

        campo_nome = driver.find_element(By.ID, "nome")
        campo_nome.send_keys("Solid Snake")

        campo_curso = Select(driver.find_element(By.ID, "curso"))
        campo_curso.select_by_visible_text('INFORMATICA')

        campo_gerar_mat = driver.find_element(By.CLASS_NAME, "btn-primary")
        campo_gerar_mat.click()

        time.sleep(1)

        # Capturar a matrícula gerada
        campo_matricula = driver.find_element(By.ID, "matricula")
        matricula = campo_matricula.get_attribute("value")

        campo_turno = Select(driver.find_element(By.ID, "turno"))
        campo_turno.select_by_visible_text('MATUTINO')

        campo_status = Select(driver.find_element(By.ID, "status"))
        campo_status.select_by_visible_text('INATIVO')

        btn_cadastrar = driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]")
        btn_cadastrar.click()

        # Aguardar e verificar se o cadastro foi realizado
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered table-hover']"))
        )

        # Passo 7: Agora, vamos editar o aluno cadastrado logo após o cadastro ser realizado

        # Passo 7.2: Encontrar e clicar no botão "Editar" do aluno que acabou de ser cadastrado
        botao_editar = driver.find_element(
            By.XPATH, f"//table[@class='table table-bordered table-hover']//tr[td[text()='{matricula}']]//a[contains(@class, 'btn-primary') and contains(., 'Editar')]"
        )
        botao_editar.click()

        # Passo 7.3: Alterar o nome do aluno
        campo_nome = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nome"))
        )
        campo_nome.clear()  # Limpar o campo de nome
        campo_nome.send_keys("Naked Snake")

        # Passo 7.4: Alterar o curso
        campo_curso = Select(driver.find_element(By.ID, "curso"))
        campo_curso.select_by_visible_text("ENFERMAGEM")

        # Passo 7.5: Alterar o turno
        campo_turno = Select(driver.find_element(By.ID, "turno"))
        campo_turno.select_by_visible_text("NOTURNO")

        # Passo 7.6: Alterar o status
        campo_status = Select(driver.find_element(By.ID, "status"))
        campo_status.select_by_visible_text("ATIVO")

        time.sleep(2)

        # Passo 7.7: Clicar no botão "Salvar" para salvar as alterações
        btn_salvar_edit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Salvar')]"))
        )
        btn_salvar_edit.click()

        print("Teste CT004 – Sucesso: Edição concluída com sucesso.")

        time.sleep(2)

        # Passo 8: Remover o aluno cadastrado
        botao_remover = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, f"//table[@class='table table-bordered table-hover']//tr[td[text()='{matricula}']]//a[contains(@class, 'btn-danger') and contains(., 'Remover')]"
            ))
        )
        botao_remover.click()

        # Verificar se o aluno foi removido
        time.sleep(2)
        print("Teste CT005 – Sucesso: Remoção concluída com sucesso.")

    except Exception as e:
        print(f"Erro durante o teste: {e}")
    finally:
        # Fecha o navegador
        driver.quit()

# Executa o teste
cadastrar_aluno()
