program p0935;

var x1, y1, x2, y2: integer;

begin
  
  readln(x1, y1, x2, y2);
  
  if ((x1 + y1) mod 2 = 0) and ((x2 + y2) mod 2 = 0) or ((x1 + y1) mod 2 > 0) and ((x2 + y2) mod 2 > 0) then
    print('YES')
  else
    print('NO');
  
end.