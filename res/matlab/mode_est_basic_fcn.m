function[mode_freq, mode_damp]=mode_est_basic_fcn(y, order)
    
    d = fdesign.lowpass(2/25, 2.5/25, 0.1, 50 );
    Hlp=design(d);
    y=filter(Hlp, y);
    y=downsample(y,10);
    
    dt=0.2;
    Len=length(y);
    u1=zeros(Len,1);
    data=iddata(y,u1,dt)
    
    na=order;
    nb=0;
    nc=order;
    nk=1; %delay
    tic
    
    sys_est = armax(data,[na nb nc nk]);
   
    [Wn,zeta]= damp(sys_est);
    [zeta,I]=sort(zeta);
    Wn=Wn(I);
    [mode_damp, I]=unique(zeta);
    mode_freq=Wn(I);
    idx=find(mode_freq<6);
    
    mode_freq=mode_freq(idx);
    mode_damp=mode_damp(idx);
end
