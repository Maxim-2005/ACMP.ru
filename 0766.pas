Program Task5;
var N, M, K:integer;
begin
Read(N,M,K);
if (N*M) = K then write('YES')
else if (N*M) < K then write('NO')
else write('YES');
end.