-- 📌 Relatório 1 — Pedidos com dados do cliente

SELECT  p.id_pedido, c.nome, p.data FROM pedido p 
JOIN cliente c ON p.id_cliente = c.id_cliente;

-- 📌 Relatório 2 — Itens de cada pedido

SELECT ip.id_pedido, pr.nome AS nome_produto, 
ip.quantidade FROM item_pedido ip JOIN produto pr 
ON ip.id_produto = pr.id_produto;

-- 📌 Relatório 3 — Pedidos de um cliente específico

SELECT id_pedido, data FROM pedido WHERE id_cliente = 10; 

--Mudar numero do id pra ver os pedidos de outros clientes.

-- 📌 Relatório 4 — Volume por pedido:

SELECT id_pedido, SUM(quantidade) AS total_itens FROM item_pedido GROUP BY id_pedido;

--📌 Relatório 5 — Produtos mais vendidos


SELECT p.nome AS produto, SUM(ip.quantidade) AS total_vendido FROM item_pedido ip JOIN produto p ON ip.id_produto = p.id_produto
GROUP BY p.nome ORDER BY total_vendido DESC;

--📌 Relatório 6 — Ranking de clientes

SELECT c.nome AS cliente, COUNT(p.id_pedido) AS total_pedidos FROM cliente c LEFT JOIN pedido p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nome ORDER BY total_pedidos DESC;

--📌 Relatório 7 — Clientes recorrentes

SELECT c.nome AS cliente, COUNT(p.id_pedido) AS total_pedidos FROM cliente c JOIN pedido p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nome HAVING COUNT(p.id_pedido) >= 10 ORDER BY total_pedidos DESC;

--📌 Relatório 8 — Produtos populares

SELECT p.nome AS produto, COUNT(ip.id_pedido) AS frequencia_pedidos FROM produto p JOIN item_pedido ip ON p.id_produto = ip.id_produto
GROUP BY p.id_produto, p.nome HAVING COUNT(ip.id_pedido) >= 100 ORDER BY frequencia_pedidos DESC;

-- 📌 Relatório 9 — Maior pedido

SELECT id_pedido, SUM(quantidade) AS volume_total FROM item_pedido
GROUP BY id_pedido HAVING SUM(quantidade) = (
    SELECT MAX(total)
    FROM ( SELECT SUM(quantidade) 
AS total FROM item_pedido GROUP BY id_pedido) AS subconsulta);

-- 📌 Relatório 10 — Cliente mais valioso


SELECT c.nome AS cliente, SUM(ip.quantidade) AS total_itens_comprados FROM cliente c JOIN pedido p ON c.id_cliente = p.id_cliente 
JOIN item_pedido ip ON p.id_pedido = ip.id_pedido GROUP BY c.id_cliente, c.nome ORDER BY total_itens_comprados DESC LIMIT 1;

-- 📌 Relatório 11 — Produtos encalhados


SELECT p.id_produto, p.nome AS produto_encalhado FROM produto p LEFT JOIN item_pedido ip ON p.id_produto = ip.id_produto
WHERE ip.id_produto IS NULL;

--📌 Relatório 12 — Cobertura de catálogo (🔥 HARD)

SELECT 
    c.nome AS cliente_premium
FROM cliente c
WHERE NOT EXISTS (
    SELECT p.id_produto 
    FROM produto p
    WHERE NOT EXISTS (
        SELECT ip.id_produto 
        FROM item_pedido ip
        JOIN pedido ped ON ip.id_pedido = ped.id_pedido
        WHERE ped.id_cliente = c.id_cliente 
          AND ip.id_produto = p.id_produto
    )
);

--💡 Desafio 13 — Top 3 produtos

SELECT p.nome AS produto, SUM(ip.quantidade) AS total_vendido FROM produto p
JOIN item_pedido ip ON p.id_produto = ip.id_produto GROUP BY p.id_produto, p.nome
ORDER BY total_vendido DESC LIMIT 3;

--💡 Desafio 14 — Cliente mais ativo por dias
SELECT c.nome AS cliente, COUNT(DISTINCT p.data) AS dias_com_pedidos FROM cliente c JOIN pedido p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nome ORDER BY dias_com_pedidos DESC LIMIT 1;

--💡 Desafio 15 — Pedidos grandes

SELECT id_pedido, COUNT(id_produto) AS total_produtos_distintos FROM item_pedido
GROUP BY id_pedido HAVING COUNT(id_produto) >= 10 ORDER BY total_produtos_distintos DESC;

-- 💡 Desafio 16 — Preferência do cliente


SELECT c.nome AS cliente, p.nome AS produto_favorito, SUM(ip.quantidade) AS quantidade_total
FROM cliente c JOIN pedido ped ON c.id_cliente = ped.id_cliente JOIN item_pedido ip ON ped.id_pedido = ip.id_pedido 
JOIN produto p ON ip.id_produto = p.id_produto GROUP BY c.id_cliente, p.id_produto ORDER BY c.nome ASC, quantidade_total DESC;

--💡 Desafio 17 — Clientes com comportamento idêntico (🔥 MUITO DIFÍCIL)

WITH CarrinhoCliente AS (
    SELECT p.id_cliente, GROUP_CONCAT (DISTINCT ip.id_produto ORDER BY ip.id_produto) AS produtos_comprados
    FROM pedido p JOIN item_pedido ip ON p.id_pedido = ip.id_pedido
    GROUP BY p.id_cliente
)
SELECT 
    c1.id_cliente AS cliente_a_id,
    cli1.nome AS cliente_a_nome,
    c2.id_cliente AS cliente_b_id,
    cli2.nome AS cliente_b_nome,
    c1.produtos_comprados

FROM CarrinhoCliente c1 JOIN CarrinhoCliente c2 ON c1.produtos_comprados = c2.produtos_comprados AND c1.id_cliente < c2.id_cliente 
JOIN cliente cli1 ON c1.id_cliente = cli1.id_cliente
JOIN cliente cli2 ON c2.id_cliente = cli2.id_cliente;