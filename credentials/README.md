Credenciais para conectar remotamente no banco. Vale tanto para executar queries num cliente SQL quanto para executar os scripts em Python.

Note que o arquivo `proxy_credentials.json` é um **template**, modifique localmente com as suas credenciais para utilizar as queries, conforme indicado abaixo.

## Para configurar a conexão local

1. Faça aqui o download do Google Cloud SQL Proxy para o Sistema Operacional adequado
2. Faça o download pelo console do Google do arquivo de credenciais para uma conta de serviço adequada
3. Substitua o conteúdo do arquivo `proxy_credentials.json` pelo conteúdo obtido no passo anterior

## Para conectar

O proxy precisa estar ativo. Execute:
> $ ./cloud_sql_proxy.exe -instances=memoriadaesgrimabrasileira:us-central1:memoriadaesgrimabrasileira=tcp:3306 -credential_file=./proxy_credentials.json
>
> (A porta TCP pode ser qualquer porta livre no computador local. Porém caso use uma porta diferente de 3306, lembre-se de atualizar também no arquivo `connect_credentials.json` para que os scripts Python conectem corretamente)

#### Para conectar com um cliente SQL

Configure uma conexão `MySQL` para `localhost`, na porta `3306` (ou outra caso tenha alterado acima).

Database: `memoriadaesgrimabrasileira`

Utilize nome de usuário e senha apropriados.

Não é necessário configurar *proxy* no cliente - o aplicativo do Google já resolve isso e basta conectar na porta local especificada. Também não é necessário utilizar `SSH` ou `SSL`.

#### Para conectar via Python

Atualize o arquivo `connect_credentials.json` com login e password.

Os scripts já estão devidamente configurados, divirta-se.
