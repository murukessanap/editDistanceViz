import matplotlib.pyplot as plt
import numpy as np
import imageio
import os


def createGIF(m,n,tmp,gif_name,d):
    # --- PARAMETERS ---
    rows, cols = m+1, n+1        # Table size
    #start_num = 1
    #save_dir = "frames"      # Temporary folder for frames
    #gif_name = "progressive_table.gif"

    # --- SETUP ---
    if not os.path.exists(tmp):
        os.makedirs(tmp)

    # --- GENERATE FRAMES ---
    num_cells = rows * cols
    frames = []
    numbers = []
    data = np.full((rows, cols), "", dtype=object)
    for k,v in d:
        i,j = k
    #for step in range(1, num_cells + 1):
        # Create data: fill numbers up to current step
        
        data[i,j] = v[0]
        #data.flat[:step] = numbers

        # Plot table
        fig, ax = plt.subplots(figsize=(cols, rows))
        ax.axis('off')

        table = ax.table(
            cellText=data,
            rowLabels=[f'M{i}' for i in range(rows)],
            colLabels=[f'N{j}' for j in range(cols)],
            loc='center',
            cellLoc='center'
        )

        table.scale(1, 1.5)
        table.auto_set_font_size(False)
        table.set_fontsize(14)

        # Save frame
        frame_path = f"{tmp}/frame_{v[1]:02d}.png"
        plt.savefig(frame_path, bbox_inches='tight', dpi=150)
        plt.close()
        frames.append(frame_path)

    print("✅ Frames generated. Creating GIF...")

    # --- CREATE GIF ---
    images = [imageio.imread(f) for f in frames]
    imageio.mimsave(gif_name, images, duration=800)  # 0.5 sec per frame

    print(f"🎬 GIF saved as '{gif_name}'")

    # --- OPTIONAL: clean up frames ---
    #for f in frames:
    #    os.remove(f)
    #os.rmdir(save_dir)
