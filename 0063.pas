program p2;

var
  S, P, X, Y: integer;

begin
  
  readln(S, P);
  
  for X := 0 to S do
  begin
    Y := S - X;
    if X * Y = P then
      begin
      writeln(X, ' ', Y);
      break;
      end;
  end;
  
end.