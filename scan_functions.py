import time

# Odorant to time
def csv_to_time(odorant_time):
    try: 
        csv_list = list(" ".join(odorant_time.strip().split())) + [" "]
        numlist = []
        num = []

        for i in csv_list:
            isnum = i.isnumeric()
            if num == [] and isnum: 
                num.append(i)
            elif isnum:
                num.append(i)
            elif num != [] and not isnum: 
                numlist.append(''.join(map(str,num)))
                num = []

        return [float(i) for i in numlist]
    except:
        print("Invalid input")
        

# River plot

def plot_river(exp, plt, np):
    # Plot river plot
    fig, ax = plt.subplots()
    #fig = plt.figure(frameon=False)
    #ax = plt.Axes(fig, [0., 0., 1., 1.])
    #fig.add_axes(ax)
    #fig.set_size_inches(5,5)

    # Plot figure (adapted from: fra_plotting.image_plot_2d(std_data,subtle=True, cmap = 'jet') )
    if type(exp) == np.ndarray:
        d_array = exp
        extent = [0, 1, 1, 0]
    else:
        d_array = exp.spectra
        extent = [np.min(exp.wavelengths), np.max(exp.wavelengths), np.max(exp.times), np.min(exp.times)]

    vmin = np.amin(d_array)
    vmax = np.amax(d_array)
    plt.imshow(d_array, vmin=vmin, vmax=vmax, interpolation='none', cmap='jet')
    
    # Define image labels
    plt.ylabel('Time (s)', fontsize=16)
    plt.xlabel('Wavelength (nm)', fontsize=16)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(axis='x',colors='black')
    ax.tick_params(axis='y',colors='black')
    
    # Image aspect ratio
    xext, yext = plt.gca().axes.get_xlim(), plt.gca().axes.get_ylim()
    xrange = xext[1] - xext[0]
    yrange = yext[1] - yext[0]
    plt.gca().set_aspect(1 * abs(xrange / yrange)) # This is the line that causes the warnings about unicode
    
    plt.tight_layout()
    
    
# Clean time

def Nitrogen(clean_time, ser, intensities, spec, delay_time):
    ser.write(b'A')

    i = 0
    start_time = time.time()
    
    while i < clean_time:
        intensities.append(spec.intensities())
        i = time.time() - start_time
        time.sleep(1/delay_time)
    
    ser.write(b'a')
    
# Scan time

def IPA(scan_time, ser, intensities, spec, delay_time):
    ser.write(b'D')

    i = 0
    start_time = time.time()
    
    while i < scan_time:
        intensities.append(spec.intensities())
        i = time.time() - start_time
        time.sleep(1/delay_time)
    
    ser.write(b'd')
    
# Water

def Water(scan_time, ser, intensities, spec, delay_time):
    
    ser.write(b'C')

    i = 0
    start_time = time.time()
    
    while i < scan_time:
        intensities.append(spec.intensities())
        i = time.time() - start_time
        time.sleep(1/delay_time)

    
    ser.write(b'c')
    

def EtOH(scan_time, ser, intensities, spec, delay_time):
    ser.write(b'B')

    i = 0
    start_time = time.time()
    
    while i < scan_time:
        intensities.append(spec.intensities())
        i = time.time() - start_time
        time.sleep(1/delay_time)
    
    ser.write(b'b')
    