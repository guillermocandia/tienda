###20140223

ALTER TABLE `tienda_order` ADD `numero_despacho` VARCHAR( 256 ) NULL DEFAULT NULL ,
ADD `comentarios` LONGTEXT NULL DEFAULT NULL ,
ADD `comentarios_interno` LONGTEXT NULL DEFAULT NULL ;

ALTER TABLE `util_aviso` CHANGE `mensaje` `mensaje` VARCHAR( 128 ) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL 
