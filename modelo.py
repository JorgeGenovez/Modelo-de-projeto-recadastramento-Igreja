import flet as ft
import pandas as pd


CadastrosPIB = pd.read_csv("Lista.csv")


TratadoCadastroPIB = CadastrosPIB.drop(columns=[
"Ramal","Pager","Tel. Comercial","Escolaridade",
"Referência", "Observações","Célula Familiar",
"Identificação", "Templo"
])

for coluna in TratadoCadastroPIB.columns:
    TratadoCadastroPIB[coluna] = TratadoCadastroPIB[coluna].apply(lambda x: x.capitalize() if isinstance(x, str) else x)

TesteCadastroPIB = TratadoCadastroPIB.drop(columns=[
    "Fotografia", "Data", "Igreja", "Pastor",
    "Situação", "Cargo Atual", "Data.1", "Modo",
    "Origem", "Data.2", "Modo.1","Destino"
])

def main(pagina):
    Rc = ft.Text("Recadastramento")
    Usuarios = ["Jorge", "Geovani"]
    Senhas = ["123", "456"]

    #Opção para menu de preenchimento automático
    # Função para atualizar sugestões
    
    sugestoes = ft.Column()

    def atualizar_sugestoes(evento):
        texto_digitado = lista_nomes.value.strip().lower()  # Captura o texto digitado na caixa de texto correta
        sugestoes.controls.clear()  # Limpa as sugestões anteriores
        
        if texto_digitado:  # Se houver texto digitado
            nomes_filtrados = [nome for nome in nomes_completos if nome.lower().startswith(texto_digitado)]
            for nome in nomes_filtrados:
                sugestao = ft.TextButton(nome, on_click=lambda e, n=nome: selecionar_nome(n))  # Cria um botão para cada nome filtrado
                sugestoes.controls.append(sugestao)  # Adiciona o botão à coluna de sugestões
        
        pagina.update()  # Atualiza a página para refletir as mudanças

    def selecionar_nome(nome):
        lista_nomes.value = nome  # Atualiza o campo de entrada com o nome selecionado
        sugestoes.controls.clear()  # Limpa as sugestões após a seleção
        pagina.update()  # Atualiza a página para refletir as mudanças


    nomes_completos = TesteCadastroPIB["Nome Completo"].tolist()
    lista_nomes = ft.TextField(label="Nome Completo", on_change=atualizar_sugestoes)

    # Tópicos do Cadastro
    matricula = ft.TextField(label="Matrícula")
    nomecompleto = ft.TextField(label="Nome")
    cpf = ft.TextField(label="CPF")
    datanascimento = ft.TextField(label="Data de Nascimento")
    tsexo = ft.Text("  Sexo")
    sexo = ft.Column([
        ft.Radio(value="Masculino", label="Masculino"),
        ft.Radio(value="Feminino", label="Feminino")
    ])
    tipo_sanguineo = ft.TextField(label="Tipo Sanguíneo")
    estado_civil = ft.TextField(label="Estado Civil")
    datacasamento = ft.TextField(label="Data do Casamento")
    profissao = ft.TextField(label="Profissão")
    naturalidade = ft.TextField(label="Naturalidade")
    nacionalidade = ft.TextField(label="Nacionalidade")
    rua = ft.TextField(label="Rua")
    complemento = ft.TextField(label="Complemento")
    bairro = ft.TextField(label="Bairro")
    municipio = ft.TextField(label="Município")
    estado = ft.TextField(label="Estado")
    cep = ft.TextField(label="CEP")
    tel_residencial = ft.TextField(label="Telefone Residencial")
    tel_celular = ft.TextField(label="Telefone Celular")
    email = ft.TextField(label="E-mail")
    nome_pai = ft.TextField(label="Nome do Pai")
    pai_membro = ft.Checkbox(label="Seu pai é membro da PIB Pavuna?")
    nome_mae = ft.TextField(label="Nome da Mãe")
    mae_membro = ft.Checkbox(label="Sua mãe é membro da PIB Pavuna?")
    nome_conjuge = ft.TextField(label="Nome do Cônjuge")
    datanascimento_conjuge = ft.TextField(label="Data de Nascimento do Cônjuge")
    conjuge_membro = ft.Checkbox(label="Seu cônjuge é membro da PIB Pavuna?")

    # Filhos
    filhos_controls = []
    for i in range(1, 6):
        filhos_controls.append(ft.TextField(label=f"Nome Filho(a) {i}"))
        filhos_controls.append(ft.TextField(label=f"Data de Nascimento do Filho(a) {i}"))
        filhos_controls.append(ft.Checkbox(label=f"Seu filho(a) {i} é membro da PIB Pavuna?"))

    def confirmando(evento):
        nomecompleto_valor = nomecompleto.value
        matricula_valor = matricula.value
        cpf_valor = cpf.value
        datanascimento_valor = datanascimento.value

        if sexo.controls[0].value:
            sexo_valor = "Masculino"
        elif sexo.controls[1].value:
            sexo_valor = "Feminino"
        else:
            sexo_valor = ""

        tipo_sanguineo_valor = tipo_sanguineo.value
        estado_civil_valor = estado_civil.value
        datacasamento_valor = datacasamento.value
        profissao_valor = profissao.value
        naturalidade_valor = naturalidade.value
        nacionalidade_valor = nacionalidade.value
        rua_valor = rua.value
        complemento_valor = complemento.value
        bairro_valor = bairro.value
        municipio_valor = municipio.value
        estado_valor = estado.value
        cep_valor = cep.value
        tel_residencial_valor = tel_residencial.value
        tel_celular_valor = tel_celular.value
        email_valor = email.value
        nome_pai_valor = nome_pai.value
        nome_mae_valor = nome_mae.value
        #---------------------
        # Crie um dicionário com os dados
        dados = {
            "Nome Completo": [nomecompleto_valor],
            "Matrícula": [matricula_valor],
            "CPF": [cpf_valor],
            "Data de Nascimento": [datanascimento_valor],
            "Sexo": [sexo_valor],
            "Tipo Sanguíneo": [tipo_sanguineo_valor],
            "Estado Civil": [estado_civil_valor],
            "Data de Casamento": [datacasamento_valor],
            "Profissão": [profissao_valor],
            "Naturalidade": [naturalidade_valor],
            "Nacionalidade": [nacionalidade_valor],
            "Rua": [rua_valor],
            "Complemento": [complemento_valor],
            "Bairro": [bairro_valor],
            "Município": [municipio_valor],
            "Estado": [estado_valor],
            "CEP": [cep_valor],
            "Tel. Residencial": [tel_residencial_valor],
            "Tel. Celular": [tel_celular_valor],
            "E-mail": [email_valor],
            "Nome do Pai": [nome_pai_valor],
            "Nome da Mãe": [nome_mae_valor],
        }
      
        df = pd.DataFrame(dados)
        df.to_csv("C:\\Users\\lucas\\OneDrive\\Documentos\\Projetos Programação\\Projetos\\Projetos para igreja\\Projeto Recadastro\\Modelo\\Lista.csv", mode='a', header=False, index=False)

        nomecompleto.value = ""
        matricula.value = ""
        cpf.value = ""
        datanascimento.value = ""
        tipo_sanguineo.value = ""
        estado_civil.value = ""
        datacasamento.value = ""
        profissao.value = ""
        naturalidade.value = ""
        nacionalidade.value = ""
        rua.value = ""
        complemento.value = ""
        bairro.value = ""
        municipio.value = ""
        estado.value = ""
        cep.value = ""
        tel_residencial.value = ""
        tel_celular.value = ""
        email.value = ""
        nome_pai.value = ""
        nome_mae.value = ""
        pagina.update()
    Confirmar = ft.ElevatedButton("Confirmar", on_click=confirmando)

    def autopreencher(evento):
        nome_inserido = lista_nomes.value.strip()  # Obter o valor do campo
        if (TesteCadastroPIB["Nome Completo"] == nome_inserido).any():
            indice = TesteCadastroPIB[TesteCadastroPIB["Nome Completo"] == nome_inserido].index[0]  # Obter o primeiro índice correspondente
            
            nomecompleto.value = TesteCadastroPIB["Nome Completo"].iloc[indice]
            matricula.value = TesteCadastroPIB["Matrícula"].iloc[indice]
            cpf.value = TesteCadastroPIB["CPF"].iloc[indice]
            datanascimento.value = TesteCadastroPIB["Data de Nascimento"].iloc[indice]
            tipo_sanguineo.value = TesteCadastroPIB["Tipo Sanguíneo"].iloc[indice]
            estado_civil.value = TesteCadastroPIB["Estado Civil"].iloc[indice]
            datacasamento.value = TesteCadastroPIB["Data de Casamento"].iloc[indice]
            profissao.value = TesteCadastroPIB["Profissão"].iloc[indice]
            naturalidade.value = TesteCadastroPIB["Naturalidade"].iloc[indice]
            nacionalidade.value = TesteCadastroPIB["Nacionalidade"].iloc[indice]
            rua.value = TesteCadastroPIB["Rua"].iloc[indice]
            complemento.value = TesteCadastroPIB["Complemento"].iloc[indice]
            bairro.value = TesteCadastroPIB["Bairro"].iloc[indice]
            municipio.value = TesteCadastroPIB["Cidade"].iloc[indice]
            estado.value = TesteCadastroPIB["Estado"].iloc[indice]
            cep.value = TesteCadastroPIB["CEP"].iloc[indice]
            tel_residencial.value = TesteCadastroPIB["Tel. Residencial"].iloc[indice]
            tel_celular.value = TesteCadastroPIB["Celular"].iloc[indice]
            email.value = TesteCadastroPIB["e-mail"].iloc[indice]
            nome_pai.value = TesteCadastroPIB["Nome do Pai"].iloc[indice]
            nome_mae.value = TesteCadastroPIB["Nome da Mãe"].iloc[indice]
            
            # Atualizar a interface se necessário
            pagina.update()


            
    
    # Criação da janela de recadastramento com scroll
    janela_recadastro = ft.AlertDialog(
    title=Rc,
    content=ft.Column(
        controls=[
            ft.Row(controls=[
                ft.Column(controls=[
                    matricula, nomecompleto, cpf,
                    datanascimento,tsexo, sexo, tipo_sanguineo, estado_civil,
                    datacasamento, profissao, naturalidade, nacionalidade,
                    rua, complemento, bairro, municipio, estado, cep, tel_residencial,
                    tel_celular, email, nome_pai, pai_membro,
                    nome_mae, mae_membro, nome_conjuge,
                    datanascimento_conjuge, conjuge_membro
                ]),
            ]),
            *filhos_controls,
            Confirmar
        ],
        scroll=True,
        width=300  # Define uma largura específica, mas ainda assim flexível
    )
    )
    pagina.overlay.append(janela_recadastro)
    # Função para abrir a janela de recadastramento
    def Recadastro(evento):
        pagina.dialog = janela_recadastro  # Atribui a janela à página
        janela_recadastro.open = True  # Abre a janela
        pagina.update()  # Atualiza a página

    Iniciar_cadastro = ft.ElevatedButton("Cadastro", on_click=Recadastro)
    Completar = ft.ElevatedButton("Autopreenchimento", on_click=autopreencher)

    # LOGIN
    def Verificar(evento):
        if Nome_usuario.value in Usuarios:
            if Senha.value in Senhas:
                if Senhas.index(Senha.value) == Usuarios.index(Nome_usuario.value):
                    print("Acesso válido")
                    Nome_usuario.value = ""
                    Senha.value = ""
                    pagina.remove(Rc)
                    pagina.remove(botao_iniciar)
                    janela.open = False
                    pagina.add(lista_nomes)
                    pagina.add(sugestoes)
                    pagina.add(Completar)
                    pagina.add(Iniciar_cadastro)
                    
                    pagina.update()
                else:
                    Senha.value = "Senha Inválida"
                    pagina.update()                 
            else:
                Senha.value = "Senha Inválida"
                pagina.update()
        else:
            Nome_usuario.value = "Usuário Inválido"
            Senha.value = ""
            pagina.update()

    titulo_janela = ft.Text("Bem-vindo ao sistema de Recadastramento")
    Nome_usuario = ft.TextField(label="Usuário")
    Senha = ft.TextField(label="Senha")
    botao_entrar = ft.ElevatedButton("Acessar Sistema", on_click=Verificar)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=ft.Column(controls=[Nome_usuario, Senha]),
        actions=[botao_entrar]
    )
    
    # Função para abrir a janela de login
    def Abrir_popup(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()   
    
    botao_iniciar = ft.ElevatedButton("Login", on_click=Abrir_popup)
    pagina.add(Rc)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)
