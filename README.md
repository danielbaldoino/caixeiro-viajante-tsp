O **problema do caixeiro viajante** (TSP - Traveling Salesperson Problem) é um dos problemas clássicos de otimização combinatória. Ele consiste no seguinte: dado um conjunto de cidades e as distâncias entre elas, determinar a rota mais curta possível que visite todas as cidades exatamente uma vez e retorne à cidade de origem.

### Características principais:
1. **Entrada:**
   - Um conjunto de cidades (n pontos) e as distâncias entre cada par de cidades.
2. **Objetivo:**
   - Encontrar a rota de menor custo (ou menor distância total).
3. **Restrições:**
   - Cada cidade deve ser visitada exatamente uma vez.
   - O ponto inicial e final da viagem deve ser o mesmo.

### Complexidade
O TSP pertence à classe de problemas NP-difíceis, ou seja, conforme o número de cidades aumenta, o tempo de resolução cresce exponencialmente. Para \(n\) cidades, o número de rotas possíveis é \((n-1)!\).

---

### Abordagens para solução:

#### 1. **Método Exaustivo (Força Bruta):**
   - Examina todas as rotas possíveis.
   - Impraticável para grandes valores de \(n\), mas garante a solução ótima.

#### 2. **Programação Dinâmica (Algoritmo de Held-Karp):**
   - Reduz a complexidade para \(O(n^2 \cdot 2^n)\), mas ainda é viável apenas para problemas pequenos.

#### 3. **Heurísticas:**
   - Oferecem boas soluções em tempo reduzido, mas sem garantia de serem ótimas.
   - Exemplos:
     - **Algoritmo do Vizinho Mais Próximo**: Começa em uma cidade e sempre vai para a mais próxima ainda não visitada.
     - **Algoritmo do Circuito Mais Barato**: Conecta pontos próximos até formar um circuito válido.

#### 4. **Meta-heurísticas:**
   - Fornecem soluções aproximadas para problemas maiores.
   - Exemplos:
     - **Algoritmo Genético**.
     - **Simulated Annealing**.
     - **Colônia de Formigas (Ant Colony Optimization)**.

#### 5. **Métodos Exatos:**
   - Baseados em **Programação Linear Inteira** ou **Branch and Bound**, que garantem a solução ótima, mas têm alta complexidade.

---

### Aplicações
O TSP é mais do que um problema teórico; ele é aplicado em diversas áreas como:
- Logística e transporte (planejamento de rotas).
- Impressão de circuitos eletrônicos.
- Planejamento de trajetos para drones.
- Serviços de entregas (ex.: otimização de rotas para entregadores).
