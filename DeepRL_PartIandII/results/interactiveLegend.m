function interactiveLegend(figure,names)
    lines = figure.Children.Children;
    len_lines = length(lines);
    len_names = length(names);
    if(len_lines < len_names)
        error("Incorrect number of inputs");
    end
    for i = 1:len_names
        NewNames(i) = cellstr(strcat(cell2mat(names(i)),' (T)'));
    end
    [leghan, objhan, plothan] = legend(NewNames, 'interpreter', 'none');
    lgd = [];
    plt = [];
    siz = length(objhan);
    c = 0;
    for p = 1:siz
        if(objhan(p-c).Type == "text")
            lgd = [lgd objhan(p-c)];
            objhan(p-c).UserData.flag = true;
            objhan(p-c).HitTest = 'on';
            objhan(p-c).ButtonDownFcn = @toggle_callback;
            objhan(p-c) = [];
            siz = siz - 1;
            c = c + 1;
        end
    end
    
    
    
    for p = 1:length(lgd)
        lgd(p).UserData.lline = findobj('Tag',strcat(cell2mat(names(p)),'_l'));
        lgd(p).UserData.lline.HitTest = 'on';
        lgd(p).UserData.lline.ButtonDownFcn = @highlight_callback;
        lgd(p).UserData.lline.UserData.flag = false;
        
        lgd(p).UserData.rline = findobj('Tag',strcat(cell2mat(names(p)),'_r'));
        lgd(p).UserData.rline.HitTest = 'on';
        lgd(p).UserData.rline.ButtonDownFcn = @highlight_callback;
        lgd(p).UserData.rline.UserData.flag = false;
    end
    
function toggle_callback(source,eventdata)
    if(source.UserData.flag)
        source.String(end-1) = 'F';
        source.UserData.lline.DisplayName(end-1) = 'F';
    else
        source.String(end-1) = 'T';
        source.UserData.lline.DisplayName(end-1) = 'T';
    end
    source.UserData.flag = ~source.UserData.flag;
    source.UserData.lline.Visible = source.UserData.flag;
    source.UserData.rline.Visible = source.UserData.flag;
    

function highlight_callback(source,eventdata)
    if(source.UserData.flag)
        source.LineWidth = source.LineWidth/4;
    else
        source.LineWidth = source.LineWidth*4;
    end
    source.UserData.flag = ~source.UserData.flag;