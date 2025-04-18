import jax
import flax as nnx
import jax.numpy as jnp
jax.random_seed(69)
def softplus(x):
  return jnp.log(1 + jnp.exp(x))
def randomplus(x):
  return jnp.log(1 + jnp.rng.uniform(x))
class Trial(nnx.Module()):
  def __init__(self):
    self.fc1 = nnx.ReLu(512)
    self.fc2 = nnx.ReLu(512)
    self.fc3 = nnx.Linear(64)
  def __call__(self,x):
    x = self.fc1(x)
    x = self.fc2(x)
    x = self.fc3(x)
    return nnx.ReLu(x) - softplus(x)
model = Tung()
