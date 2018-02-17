: star      [char] * emit ;
: stars     0 ?DO star LOOP ;
: margin    CR 30 spaces ;
: bar       margin 5 stars ;
: blip      margin star ;
: F         bar blip bar blip blip ;
