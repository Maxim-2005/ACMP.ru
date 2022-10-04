program p0026;

var
  x1, y1, r1, x2, y2, r2: integer;
  g: real;

begin
  readln(x1, y1, r1);
  readln(x2, y2, r2);
  
  g := sqrt(sqr(x2 - x1) + sqr(y2 - y1));
  
  if (r1 + r2 >= g) and (abs(r1 - r2) <= g) then
    writeln('YES')
  else
    writeln('NO');
end.