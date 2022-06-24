
CREATE TABLE `api_trips` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `region` varchar(50) NOT NULL,
  `origin_coord` varchar(200) NOT NULL,
  `destination_coord` varchar(200) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `datasource` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8

CREATE TABLE `api_trips_group` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `region` varchar(50) NOT NULL,
  `origin_coord` varchar(200) NOT NULL,
  `destination_coord` varchar(200) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `datasource` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
