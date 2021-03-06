        Nmap:

Scan de portas e seus serviços:

nmap -p(porta) -sV (url)

Scan de portas abertas:

nmap (url)

Scan de portas e seus serviços diretamente:

nmap -v -sV (url)

Scan Bruto:

nmap --script vuln -v -sV (url)

Scan do Sistema Oparacional:

nmap -O (url)

Scan agresivo:

nmap -A (url)

Scan anonimo:

é so colocar -sS depois do nmap ou seja 

nmap -sS ...

pingar usando o nmap:

nmap -sP 108.179.193.118

Comandos e suas funções

VERIFICAÇÃO BÁSICA

Digitalizar um objetivo                                          |  nmap [target]              
Digitalização de múltiplos objetivos                    |  nmap [target1,target2,etc]
Digitalizar uma lista de objetivo                           |  nmap -IL [list.txt]
Digitalize uma variedade de hospedeiros            | nmap [range of IP addresses]
Digitalizar uma sub-rede inteira                           |  nmap -iR [number]
Excluindo-se os objetivos de uma varredura       | nmap [targets] –exclude [targets] 
Excluindo-se os objetivos por meio de uma lista | nmap [targets] –excludefile [list.txt]
Realizar uma exploração agressiva          |  nmap -A [target]
Digitalizar um alvo IPv6                | nmap -6 [alvo]

OPÇÕES DE DESCOBERTA 

Execute somente um Ping exploração      |  nmap -sP [alvo]
Não pingue                                                         |   nmap -PN [target]
TCP SYN Ping                                            |  nmap -PS [target]
TCP ACK Ping                                           |   nmap -PA [target]
UDP Ping                                                    |   nmap -PU [target]
SCTP Init Ping                 |    nmap -PY [target]
Eco ICMP Ping                       |   nmap -PE [target]
ICMP Timestamp Ping                |    nmap -PP [target]
Ping ICMP máscara de endereço               |   nmap -PM [target]
Protocolo IP Ping                      |    nmap -PO [target]
ARP Ping                            |   nmap -PR [target]
Traceroute                 |    nmap -traceroute [target]
Força DNS resolução inversa                 |   nmap -R [target]
Desativar a resolução de DNS reverso       |    nmap -n [target]
Pesquisa de DNS alternativo                     |   nmap -system-dns [target]
Especificar manualmente os servidores DNS  |   nmap -dns-servers [servers] [target]
Criar uma lista de acolhimento           |  nmap -SL [target]

RESOLUÇÃO DE PROBLEMAS E DEPURAMENTO 

Ajuda                                      |  nmap -h
Exibe a versão do Nmap          |   nmap -V
Exibe os resultados detalhados            | nmap -v [alvo]
Depuração               |   nmap-d [alvo]
Mostrar pelo Estado do porto              | nmap –reason [target]
Rastreamento de pacotes          | nmap-packet-trace [alvo]

NMAP SCRIPTING ENGINE

Executar scripts individuais                             |  nmap –script [script.nse] [target]   
Executar vários scripts                                    |   nmap –script [expression] [target]     
Executar scripts por categorias         | nmap –script [category] [target]
Solucionar problemas de scripts       |   nmap –script [script] –script-trace [target]

EVASÃO DE FIREWALL 

Randomize ordem de análise objetiva            |  nmap –randomize-hosts [target]
Spoof MAC Address            |    nmap –spoof-mac [MAC|0|vendor] [target]