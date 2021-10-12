program Task;
var X,Y,Z,Max,Min:integer;
begin
read(X,Y,Z);
 
if (X > 100000) or (Y > 100000) or (Z > 100000) then exit;
 
if (X >= Y) and (X >= Z) then Max := X
else if (Y >= X) and (Y >= Z) then Max := Y
else if (Z >= X) and (Z >= Y) then Max := Z;
 
if (X <= Y) and (X <= Z) then Min := X
else if (Y <= X) and (Y <= Z) then Min := Y
else if (Z <= X) and (Z <= Y) then Min := Z;
 
write(Max-Min);
end.