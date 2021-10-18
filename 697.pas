program p1;

var L, W, H, S, B : integer;

begin
  
  readln(L, W, H);
  S := (L + W) * H * 2;
  B := S div 16;
  
  if S mod 16 > 0 then
    B := B + 1;
  
  writeln(B);
  
end.