program p1;

var
  N: int64;

begin
  readln(N);

  if N > 2 then
    write(N * (N - 1) * (N - 2))
  else
    write(N);

end.