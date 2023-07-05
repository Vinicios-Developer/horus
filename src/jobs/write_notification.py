def write_notification(email: str, mensagem=''):
    with open ('log.txt', mode='w') as email_file:
        conteudo = f"Notificação para {email}: {mensagem}"
        email_file.write(conteudo) 