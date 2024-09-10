<h1>
  Desenvolvedor:
</h1>
<h5>
  - Nano
</h5>


<center>
  <h1>
    Sobre o script:
  </h1>
</center>

<h4>
  - Script desenvolvido por Nano e sua função é a quebra de hashes do tipo, MD5,MD4,SHA1,SHA512,SHA384 e etc.<br>
  - Script focado em descobrimento de hashes<br>
  - Atualmente ele carrega 2 wordlists.txt com milhares de senhas que foram vazadas pela internet<br>
  - Depende do poder de processamento, quanto mais forte, mais rápido será para carregar e comparar as wordlists<br>
</h4>

<h1>
  Sobre sites, apis e wordlist do scripts:
</h1>

<h4>
  - Antes de abrir as wordlists, o script tentará utilizar sites e apis para tentar descobrir a senha da hash<br>
  - Caso ele não consiga por nenhum dos sites, ele irá abrir as duas wordlists e tentar encontrar por elas
</h4>

<h1>
  Como funciona o script:
</h1>
<h4>
  - Atualmente a lógica que eu desenvolvi para isso, foi carregar cada senha da wordlist e convertê-la no tipo de hash que o script retornar<br>
  - Após a conversão, ele vai percorrer toda a wordlist e fazer a comparação de hash, caso a hash seja idêntica a uma gerada pelo script nas wordlists
  ele retorna a hash e a senha correspondente para a sua hash!<br>
</h4>

<h1>
  Modo de uso:
</h1>
  
<h4>
  - python hash.py sua hash aqui
</h4>
<h1>
  Livre arbítrio:
</h1>

<h4>
  - Se você souber a linguagem do script, você poderá modificar o que achar que deve modificar!<br>
  - Fique a vontade para adicionar senhas nas wordlists, assim ela nunca ficará ultrapassada!<br>
</h4>
