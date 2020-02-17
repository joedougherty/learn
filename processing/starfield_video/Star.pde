class Star {
 float x, y, z;
 
 Star() {
  x = random(-width, width);
  y = random(-height, height);
  z = random(width);
 }
 
 void update(float spd) {
    z = z - spd;
   
    if (z < 1) {
      z = width;
      x = random(-width, width);
      y = random(-height, height);
    }
 }
 
 void show(int s_color, float force_multiplier) {
   fill(s_color);
   noStroke();
   
   float sx = map(x / z, 0, 1, 0, width);
   float sy = map(y / z, 0, 1, 0, height);
 
   float r = map(z, 0, width, 9*force_multiplier, 0);  
   
   ellipse(sx, sy, r, r);
 }
}
