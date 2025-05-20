% Get a LIDAR Scan
% Returns a range vector of 682 elements after a Lidar Scan from min step
% to max step.
% Range Values correspond from -120 to +120 degrees.
% Author- Shikhar Shrestha, IIT Bhubaneswar
function [rangescan]=LidarScan(lidar)
proceed=0;
while (proceed==0)
fprintf(lidar,'GD0044072500');
pause(0.01);

data=fscanf(lidar);
if numel(data)==2134
    proceed=1;
end

end

i=find(data==data(13));
rangedata=data(i(3)+1:end-1);
for j=0:31
onlyrangedata((64*j)+1:(64*j)+64)=rangedata(1+(66*j):64+(66*j));
end
j=0;
for i=1:floor(numel(onlyrangedata)/3)
encodeddist(i,:)=[onlyrangedata((3*j)+1) onlyrangedata((3*j)+2) onlyrangedata((3*j)+3)];
j=j+1;
end
for k=1:size(encodeddist,1)
    rangescan(k)=decodeSCIP(encodeddist(k,:));
end

function val = decodeSCIP(chars)
% Decodifica un valor de distancia codificado en 3 caracteres ASCII
    val = 0;
    for i = 1:3
        val = bitshift(val, 6) + (double(chars(i)) - 0x30);
    end
end
end