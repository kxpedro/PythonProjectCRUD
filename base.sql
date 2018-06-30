USE projeto;

CREATE TABLE carro(
    id INT auto_increment,
    marca VARCHAR(100),
    ano DATE,
    valor DECIMAL(12,2),
    foto VARCHAR(100),

    primary key(id)
);