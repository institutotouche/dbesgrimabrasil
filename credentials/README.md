Credenciais para conectar remotamente no banco. Vale tanto para executar queries num cliente SQL quanto para executar os scripts em Python.

Note que o arquivo `proxy_credentials.json` é um **template**, modifique localmente com as suas credenciais para utilizar as queries, conforme indicado abaixo.

## Para conectar

1. Faça aqui o download do Google Cloud SQL Proxy para o Sistema Operacional adequado
2. Faça o download pelo console do Google do arquivo de credenciais para uma conta de serviço adequada
3. Substitua o conteúdo do arquivo `proxy_credentials.json` pelo conteúdo obtido no passo anterior
4. Também no console do Google, obtenha o *instance name* para acesso.
5. Execute:
> $ ./cloud_sql_proxy.exe -instances=< instance name >=tcp:3306 -credential_file=./proxy_credentials.json
>
> (A porta TCP pode ser qualquer porta livre no computador local. Porém caso use uma porta diferente de 3306, lembre-se de atualizar também nos arquivos de configuração dos scripts Python para conectar corretamente)
