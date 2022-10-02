Program p0844;

var a, b: int64;

begin
  readln(a, b);
  
  if frac(sqrt(a * b)) = 0 then
    writeln(sqrt(a * b))
  else
    writeln(0);
  
end.