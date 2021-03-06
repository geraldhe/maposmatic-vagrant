CREATE OR REPLACE VIEW planet_osm_point AS
SELECT
osm_id,
tags->'access' as "access",
tags->'addr:housename' as "addr:housename",
tags->'addr:housenumber' as "addr:housenumber",
tags->'admin_level' as "admin_level",
tags->'aerialway' as "aerialway",
tags->'aeroway' as "aeroway",
tags->'amenity' as "amenity",
tags->'barrier' as "barrier",
tags->'boundary' as "boundary",
tags->'building' as "building",
tags->'capital' as "capital",
tags->'denomination' as "denomination",
tags->'ele' as "ele",
osm_tag2num(tags->'ele') as "num_ele",
tags->'generator:source' as "generator:source",
tags->'highway' as "highway",
tags->'historic' as "historic",
tags->'iata' as "iata",
tags->'junction' as "junction",
tags->'landuse' as "landuse",
tags->'leisure' as "leisure",
tags->'man_made' as "man_made",
tags->'military' as "military",
tags->'name' as "name",
tags->'name:de' as "name:de",
tags->'int_name' as "int_name",  
tags->'name:en' as "name:en",
tags->'natural' as "natural",
tags->'operator' as "operator",
tags->'place' as "place",
tags->'population' as "population",
tags->'power' as "power",
tags->'power_source' as "power_source",
tags->'railway' as "railway",
tags->'ref' as "ref",
tags->'religion' as "religion",
tags->'ruins' as "ruins",
tags->'service' as "service",
tags->'shop' as "shop",
tags->'sport' as "sport",
tags->'tourism' as "tourism",
tags->'waterway' as "waterway",
tags->'wetland' as "wetland",
osm_tag2num(tags->'width') as "num_width",
way as "way",
z_order as z_order,
osml10n_get_placename_from_tags(tags,true,false,chr(10),'de',way) as localized_name_second,
osml10n_get_placename_from_tags(tags,false,false,chr(10),'de',way) as localized_name_first,
osml10n_get_name_without_brackets_from_tags(tags,'de',way) as localized_name_without_brackets,
osml10n_get_streetname_from_tags(tags,true,false,chr(10),'de', way) as localized_streetname,
COALESCE(tags->'name:hsb',tags->'name:dsb',tags->'name') as name_hrb,
layer as layer,
tags as "tags",
tags->'disused' as "disused",
tags->'lock' as "lock",
tags->'station' as "station",
tags->'public_transport' as "public_transport",
tags->'subway' as "subway",
tags->'direction' as "direction",
tags->'otm_isolation' as "otm_isolation",
tags->'train' AS "train",
tags->'summit:cross' AS "summit:cross",
tags->'memorial:type' AS "memorial:type",
tags->'castle_type' AS "castle_type",
tags->'leaf_type' AS "leaf_type",
tags->'denotation' AS "denotation",
tags->'tower:type' AS "tower:type",
tags->'communication:radio' AS "communication:radio",
tags->'communication:television' AS "communication:television",
tags->'site_type' AS "site_type",
tags->'abandoned' AS "abandoned",
tags->'office' AS "office",
tags->'harbour' AS "harbour",
tags->'bus' AS "bus",
tags->'bicycle' AS "bicycle",
tags->'covered' AS "covered"
FROM planet_osm_hstore_point;

GRANT select ON planet_osm_point TO public;
