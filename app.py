import os

contact = { "name": "Wanderson Passos Barcelos", 
           "phone": "27999447975", 
           "email": "wpbarcelos@gmail.com", 
           "favorite": False 
           }
agenda = [contact]

def input_field(placeholder=""):
    value=''
    while True:
        value = input(placeholder)
        if value:
            break
    return value


def show_menu():
    
    
        
    print("Menu de app_contatos:")
    print("1 - para adicionar um contato")
    print("2 - para visualizar a lista de contatos cadastrados")
    print("3 - editar um contato")
    print("4 - marcar/desmarcar um contato como favorito")
    print("5 - listar contatos favoritos")
    print("0 - para sair")
    
def add_contact(agenda):

    try:
        print("\nAdiciona contato: ")
        name = input_field("Nome: ")
        phone = input_field("Telefone: ")
        email = input_field("Email: ")

        contact = { "name": name, "phone": phone, "email": email, "favorite": False}
        agenda.append(contact)
        print("O Contato adicionado na agenda.")
    except Exception  as e:
        print(f"Ocorreu um erro ao adicionar contato {e}")

def list_all_contacts(agenda):
    
    print("\nLista de todos os contatos\n")
    
    try: 
    
        index = 0
        for contact in agenda:
            index = index+1
            is_favorite = "Sim" if contact['favorite'] else 'Não'
            
            print(f"# {index}")
            print(f"Nome: {contact["name"]} ")
            print(f"Telefone: {contact["phone"]}")
            print(f"E-mail: {contact["email"]}")
            print(f"Favorito: {is_favorite}")
            print("=====\n")
    except Exception as e:
        print(f"Erro ao imprimir lista: {e}")    
        
def edit_contact(agenda):
    
    index = int(input("Informe o codigo do contato or '0' para voltar ao menu: "))
    
    if index == 0:
        return
    
    try:
        if not agenda[index-1] :
            print("Codigo não existe na agenda tente novamente.")
            return edit_contact(agenda)
        
        contact = agenda[index -1]
        print(contact['name'])
        
        contact['name'] = input(f"Informe o novo nome ou {contact['name']}: ") or contact['name']
        contact['phone'] = input(f"Informe o novo telefone ou {contact['phone']}: ") or contact['phone']
        contact['email'] = input(f"Informe o novo email ou  {contact['email']}: ") or contact['email']
        
        agenda[index-1] = contact
    except Exception as e:
        print(f"Erro ao editar {e}")
    
def toggle_favorite(agenda):    

    index = int(input("Informe o codigo do contato adicionar/remover favorito ou '0' para voltar ao menu: "))
    
    if index == 0:
        return
    if not agenda[index-1]:
        return toggle_favorite(agenda)
    
    index = index-1
    
    is_favorite = bool(agenda[index]['favorite'])
    agenda[index]['favorite']  = not is_favorite
    
    operation = "removido de" if is_favorite else "adicionado em"
    
    print(f"{agenda[index]['name']} foi {operation} favoritos\n")


def list_favorites(agenda):
    print("\n *** Contatos favoritos *** ")
    
    try: 
    
        index = 0
        for contact in agenda:
            index = index+1
            if contact['favorite']:
                print(f"# {index}")
                print(f"Nome: {contact["name"]} ")
                print(f"Telefone: {contact["phone"]}")
                print(f"E-mail: {contact["email"]}")
                print("=====\n")
    except Exception as e:
        print(f"Erro ao imprimir lista: {e}")    
    
def clear_terminal():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
            
clear_terminal()

while True:

   
    show_menu()
    
    menu = int(input("opção: "))
    
    clear_terminal()
    
 
    try:
        if menu == 0:
            break
        elif menu == 1:
            add_contact(agenda)
        elif menu == 2:
            list_all_contacts(agenda)
        elif menu == 3:
            edit_contact(agenda)
        elif menu == 4:
            toggle_favorite(agenda)
        elif menu == 5:
            list_favorites(agenda)
        
    except Exception as e:
        print("\nOcorreu um erro tente novamente. {e}")
        

        
# ###
# - [x] Deve ser possível adicionar um contato
#     - O contato pode ter os dados:
#     - Nome
#     - Telefone
#     - Email
#     - Favorito (está opção é para poder marcar um contato como favorito)
# - [x] Deve ser possível visualizar a lista de contatos cadastrados
# - Deve ser possível editar um contato
# - Deve ser possível marcar/desmarcar um contato como favorito
# - Deve ser possível ver uma lista de contatos favoritos
# - Deve ser possível apagar um contato
# ###        
