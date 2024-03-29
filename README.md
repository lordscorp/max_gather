**Otimizador de Coleta - API**
----
Calcula o número máximo de frutas que podem ser coletadas em determinados intervalos de um array de inteiros.

Retorna objeto `json` com:
 - Número máximo de frutas coletadas
 - Índice do array do início da primeira coleta
 - Índice do array do início da segunda coleta

```json
{
  "data": [2, 0, 1]
}
```

Caso não seja informado um intervalo válido para coleta, retorna "-1" como primeiro valor do objeto "data" (número máximo de frutas).

##Configuração do servidor

É necessário ter o `pipenv` instalado para instalar a aplicação.

### Instalar dependências
```
pipenv install
```
### Iniciar aplicação
```
flask run --host=0.0.0.0 --port=8080
```

---

##Especificações

* **URL**

  /

* **Method:**

  `POST`
  
* **Data Params**

  **Required:**

  `A=[array(integer, integer, ...)]`
  `K=[integer]`
  `L=[integer]`


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "data": [42,0,4] }`
 
* **Sample Call:**

  ```javascript
  let pData = new FormData();
      pData.append('A', [15,2,2,3,5,1,19])
      pData.append('K', 2)
      pData.append('L', 3)
      axios.post('/', postBody)
      .then((response) => {
          this.gathering = response.data;          
      })
  ```
