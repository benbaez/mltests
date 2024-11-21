# mltests

## Various scripts for ML testing

### stable-diffusion-stress.py for simulating stressing GPU in a more real load.

### c10 CUDA error replication

Script to replicate below error, usually within 5 attempts.

```
RuntimeError: CUDA error: an illegal instruction was encountered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

2023-07-20 22:50:00,580: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing the engine
2023-07-20 22:50:00,580: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback TensorboardLogger
2023-07-20 22:50:00,580: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback ConsoleLogger
2023-07-20 22:50:00,580: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback SpeedMonitor
2023-07-20 22:50:00,580: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback LRMonitor
2023-07-20 22:50:00,580: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback MemoryMonitor
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback RuntimeEstimator
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Closing callback CheckpointSaver
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback TensorboardLogger
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback ConsoleLogger
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback SpeedMonitor
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback LRMonitor
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback MemoryMonitor
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback RuntimeEstimator
2023-07-20 22:50:00,581: rank3[181][MainThread]: DEBUG: composer.core.engine: Post-closing callback CheckpointSaver
terminate called after throwing an instance of 'c10::Error'
  what():  CUDA error: an illegal instruction was encountered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:44 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7fff603674d7 in /usr/lib/python3/dist-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x64 (0x7fff6033136b in /usr/lib/python3/dist-packages/torch/lib/libc10.so)
frame #2: c10::cuda::c10_cuda_check_implementation(int, char const*, char const*, int, bool) + 0x118 (0x7fff60403b58 in /usr/lib/python3/dist-packages/torch/lib/libc10_cuda.so)
frame #3: c10d::ProcessGroupNCCL::WorkNCCL::finishedGPUExecutionInternal() const + 0x80 (0x7fff617d7ee0 in /usr/lib/python3/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: c10d::ProcessGroupNCCL::WorkNCCL::isCompleted() + 0x58 (0x7fff617db4b8 in /usr/lib/python3/dist-packages/torch/lib/libtorch_cuda.so)
frame #5: c10d::ProcessGroupNCCL::workCleanupLoop() + 0x227 (0x7fff617dca07 in /usr/lib/python3/dist-packages/torch/lib/libtorch_cuda.so)
frame #6: <unknown function> + 0xd6de4 (0x7fffcceafde4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #7: <unknown function> + 0x8609 (0x7ffff7db8609 in /usr/lib/x86_64-linux-gnu/libpthread.so.0)
frame #8: clone + 0x43 (0x7ffff7ef2133 in /usr/lib/x86_64-linux-gnu/libc.so.6)
```
