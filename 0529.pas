program p1;

var X1, Y1, X2, Y2, S, a, b, c, d :real;

begin
  
  readln(X1, Y1, X2, Y2);
  
  a := X1 - X2;
  b := Y1 - Y2;
  
  S := sqrt(a * a + b * b);
  
  Writeln(S:0:5);
  
end.