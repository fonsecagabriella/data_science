import matplotlib.pyplot as plt
import numpy as np
import glob
from matplotlib import image
import cv2


def load_images(directory):
    images = []
    for filename in glob.glob(directory+'*.jpg'):
        img = np.array(image.imread(filename))
        gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        images.append(gimg)

        height, width = gimg.shape
        
    return images

def plot_reduced_data(X):
    plt.figure(figsize=(12,12))
    plt.scatter(X[:,0], X[:,1], s=60, alpha=.5)
    for i in range(len(X)):
        plt.text(X[i,0], X[i,1], str(i),size=15)
    plt.show()

def plot_lines(M):
    x_1 = np.linspace(-10,10,100)
    x_2_line_1 = (M[0,2] - M[0,0] * x_1) / M[0,1]
    x_2_line_2 = (M[1,2] - M[1,0] * x_1) / M[1,1]
    
    _, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x_1, x_2_line_1, '-', linewidth=2, color='#0075ff',
        label=f'$x_2={-M[0,0]/M[0,1]:.2f}x_1 + {M[0,2]/M[0,1]:.2f}$')
    ax.plot(x_1, x_2_line_2, '-', linewidth=2, color='#ff7300',
        label=f'$x_2={-M[1,0]/M[1,1]:.2f}x_1 + {M[1,2]/M[1,1]:.2f}$')

    A = M[:, 0:-1]
    b = M[:, -1::].flatten()
    d = np.linalg.det(A)

    if d != 0:
        solution = np.linalg.solve(A,b) 
        ax.plot(solution[0], solution[1], '-o', mfc='none', 
            markersize=10, markeredgecolor='#ff0000', markeredgewidth=2)
        ax.text(solution[0]-0.25, solution[1]+0.75, f'$(${solution[0]:.0f}$,{solution[1]:.0f})$', fontsize=14)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xticks(np.arange(-10, 10))
    ax.set_yticks(np.arange(-10, 10))

    plt.xlabel('$x_1$', size=14)
    plt.ylabel('$x_2$', size=14)
    plt.legend(loc='upper right', fontsize=14)
    plt.axis([-10, 10, -10, 10])

    plt.grid()
    plt.gca().set_aspect("equal")

    plt.show()



def string_to_augmented_matrix(equations):
    # Split the input string into individual equations
    equation_list = equations.split('\n')
    equation_list = [x for x in equation_list if x != '']
    # Create a list to store the coefficients and constants
    coefficients = []
    
    ss = ''
    for c in equations:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in ss:
                ss += c + ' '
    ss = ss[:-1]
    
    # Create symbols for variables x, y, z, etc.
    variables = symbols(ss)
    # Parse each equation and extract coefficients and constants
    for equation in equation_list:
        # Remove spaces and split into left and right sides
        sides = equation.replace(' ', '').split('=')
        
        # Parse the left side using SymPy's parser
        left_side = sympify(sides[0])
        
        # Extract coefficients for variables
        coefficients.append([left_side.coeff(variable) for variable in variables])
        
        # Append the constant term
        coefficients[-1].append(int(sides[1]))

    # Create a matrix from the coefficients
    augmented_matrix = Matrix(coefficients)
    augmented_matrix = np.array(augmented_matrix).astype("float64")

    A, B = augmented_matrix[:,:-1], augmented_matrix[:,-1].reshape(-1,1)
    
    return ss, A, B


def plot_transformation(T,v1,v2, vector_name='v'):
    color_original = "#129cab"
    color_transformed = "#cc8933"
    
    v1_transformed = T @ v1
    v2_transformed = T @ v2
    
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    vmin = np.floor(np.min([v1,v2, v1_transformed, v2_transformed, (v1_transformed + v2_transformed)]) - 0.5)
    vmax = np.ceil(np.max([v1,v2, v1_transformed, v2_transformed, (v1_transformed + v2_transformed)]) + 0.5)
    ax.set_xticks(np.arange(vmin, vmax))
    ax.set_yticks(np.arange(vmin, vmax))
    plt.axis([vmin, vmax, vmin, vmax])
    
    plt.quiver([0, 0],[0, 0], [v1[0], v2[0]], [v1[1], v2[1]], color=color_original, angles='xy', scale_units='xy', scale=1)
    plt.plot([0,v2[0],v1[0]+v2[0],v1[0]], 
        [0,v2[1],v1[1]+v2[1],v1[1]], 
        color=color_original)
    
    v1_sgn = 0.02 * (vmax-vmin) * np.array([[1] if i==0 else [i] for i in np.sign(v1)])
    ax.text(v1[0] + v1_sgn[0], v1[1], f'${vector_name}_1$', fontsize=14, color=color_original)
    
    v2_sgn = 0.02 * (vmax-vmin) * np.array([[1] if i==0 else [i] for i in np.sign(v2)])
    ax.text(v2[0], v2[1] + v2_sgn[1], f'${vector_name}_2$', fontsize=14, color=color_original)
    
    
    plt.quiver([0, 0],[0, 0], [v1_transformed[0], v2_transformed[0]], [v1_transformed[1], v2_transformed[1]], 
               color=color_transformed, angles='xy', scale_units='xy', scale=1)
    plt.plot([0,v2_transformed[0],v1_transformed[0]+v2_transformed[0],v1_transformed[0]], 
             [0,v2_transformed[1],v1_transformed[1]+v2_transformed[1],v1_transformed[1]], 
             color=color_transformed)
    
    v1_transformed_sgn = 0.04 * (vmax-vmin) * np.array([[1] if i==0 else [i] for i in np.sign(v1_transformed)])
    ax.text(v1_transformed[0] + v1_transformed_sgn[0] - 0.1 * (1 if v1_transformed[0]<0  else 0), 
            v1_transformed[1] - v1_transformed_sgn[1] - 0.05 * (1 if v1_transformed[1]<0 else 0), 
            f'$T({vector_name}_1)$', fontsize=14, color=color_transformed)
    
    v2_transformed_sgn = 0.04 * (vmax-vmin) *np.array([[1] if i==0 else [i] for i in np.sign(v2_transformed)])
    ax.text(v2_transformed[0] + v2_transformed_sgn[0] - 0.1 * (1 if v1_transformed[0]<0 else 0),  
            v2_transformed[1] - v2_transformed_sgn[1] - 0.05 * (1 if v1_transformed[1]<0 else 0), 
            f'$T({vector_name}_2)$', fontsize=14, color=color_transformed)
    
    
    plt.gca().set_aspect("equal")
    plt.show()
    return fig