use bd_recetas;
drop table datos;
drop table datost;
drop table datosingre;
CREATE TABLE datos (
    id int NOT null AUTO_INCREMENT,
    link varchar(255) not null,
    chocolate varchar(255) not null,
    harina varchar(255) not null,
    leche varchar(255) not null,
    huevo varchar(255) not null,
    azucar varchar(255) not null,
    sal varchar(255) not null,
    mantequilla varchar(255) not null,
    polvo varchar(255) not null,
    marihuana varchar(255) not null,
    cocoa varchar(255) not null,
    PRIMARY key (id)
);


CREATE TABLE datosIngre (
    id int NOT null AUTO_INCREMENT,
    link varchar(255) not null,
    ingrediente varchar(255) not null,
    costo varchar(255) not null,
    PRIMARY key (id)
);

CREATE TABLE datosT (
    id int NOT null AUTO_INCREMENT,
    link varchar(255) not null,
    ingredientes varchar(255) not null,
    costo varchar(255) not null,
    tiempo varchar(255) not null,
    personas varchar(255) not null,
    name varchar(255) not null,
    PRIMARY key (id)
);