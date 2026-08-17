import os

os.makedirs('test', exist_ok=True)
for i in range(5):
    with open(f'test/file{i}.txt', 'w') as f:
        f.write(f'Test content for file {i}\n')
print('Test directories and files created!')