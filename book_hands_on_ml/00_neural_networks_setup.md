# Common Activation Functions in Neural Networks

| Activation Function | Use Case                                                                                 | Implementation Example                  |
|---------------------|-------------------------------------------------------------------------------------------|-----------------------------------------|
| **ReLU**            | Default for hidden layers; works well in most deep networks.                             | `activation='relu'`                     |
| **LeakyReLU**       | Variation of ReLU to avoid "dying neurons" (gradient becomes zero for some neurons).      | `activation='leaky_relu'`               |
| **Sigmoid**         | Good for binary classification output (e.g., 0 or 1).                                    | `activation='sigmoid'`                  |
| **Tanh**            | Used for hidden layers; outputs between -1 and 1, centered at zero.                      | `activation='tanh'`                     |
| **Softmax**         | Multi-class classification output (e.g., 3 or more categories).                          | `activation='softmax'`                  |
| **Swish**           | Useful for deep networks; improves training and generalization (often better than ReLU). | `activation='swish'`                    |
| **SELU**            | Self-normalizing networks; requires specific initializers like Lecun Normal.             | `activation='selu'`                     |
| **ELU**             | Alternative to ReLU, avoids dying neurons, and can handle small negative inputs better.   | `activation='elu'`                      |
| **Linear**          | Default for regression tasks; outputs unbounded values.                                  | `activation='linear'`                   |

---

### Notes
- **Swish** is defined as \( f(x) = x \cdot \text{sigmoid}(x) \), and it's smooth and non-monotonic, making it suitable for advanced architectures.
- For most classification tasks, start with ReLU for hidden layers and Sigmoid or Softmax for the output layer.
- Experiment with advanced activations like Swish, LeakyReLU, or ELU if ReLU underperforms.


# Common Initializers in Neural Networks

| Initializer         | Use Case                                                                 | Implementation Example                                |
|---------------------|--------------------------------------------------------------------------|-----------------------------------------------------|
| **Glorot (Xavier)** | Default for most layers, especially in fully connected and softmax layers. | `kernel_initializer='glorot_uniform'`              |
| **He**              | Best for layers with ReLU or variants (e.g., LeakyReLU, SELU).           | `kernel_initializer='he_normal'`                   |
| **Lecun**           | Best for layers with SELU activation (self-normalizing networks).        | `kernel_initializer='lecun_normal'`                |
| **Random Uniform**  | Simple initialization, useful for experimentation.                      | `kernel_initializer='random_uniform'`              |
| **Random Normal**   | Initializes weights from a normal distribution.                         | `kernel_initializer='random_normal'`               |
| **Zeros**           | Rarely used, sets all weights to zero (useful for debugging).            | `kernel_initializer='zeros'`                       |
| **Ones**            | Rarely used, initializes all weights to one (mostly for debugging).      | `kernel_initializer='ones'`                        |

---

### Notes
- The default initializer in Keras is typically Glorot Uniform.
- Choose an initializer based on the activation function for optimal performance.



