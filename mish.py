import jax
import jax.numpy as jnp
paper = 'https://arxiv.org/abs/1908.08681'
def mish(x:ArrayLike) -> Array:
    x = jnp.asarray(x)
    return x * jnp.tanh(jax.nn.softplus(x))
# More info can be found on the paper