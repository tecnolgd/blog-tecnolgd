[← Home](../index.md)

## From local builds to pip install - repoScanner-v.0.3.0-beta.9
*Aug xx, 2026 | Category: tools/build

It's been quite a few days since I released the latest version of `repoScanner` with `pip` installation with it. It was a very tiresome version to work on 'cause I planned to include prebuilt executables and make the tool usable with just a `pip install repoScanner` and guess what, it was very satisfying to watch it work on a completely different folder with good performance numbers. What was also interesting is, I gained invaluable knowledge and first-hand experience on how to make the tool usable with the least amount of friction.

### The Origins - Why `pip install`

When my tool was ready and usable, I felt the work is done. But, I thought what if somebody wants to use the tool, not contribute or try to understand in depth what it does? Then came the idead of making the tool installable in a single command. I did a bit of research and figured out that since the project was python-based when it started, i thought of makinf sure the tool could be installed using `pip` so the users get the performace of my native cpp library engine(libcvault) ad also be able to use it without any gcc or make.

### The Plan - using buildwheels

Now I had decided what should be done, I went to do some research on what should be the approach taken to make the tool pip installable and also make sure the binaries are available with the libcvault cpp features as well(well, at least for linux environments) with the mac and windows getting the native python executables. The steps I had to follow were as follows:   

- Create cibuildwheels for the cpp library based binary for the linux users and normal binaries for mac and windows users
- Make sure they update on every tag release and get published automatically to pypi index
- Make the process automated via a build and publish pipeline utilising ci cd

As per my plan, I made the pypi publish operation to be invoked only when a new tag is released and kept the latest fallback to avoid buggy versions. The `publish.yml` code snippet is as follows:
```yml
   name: Publish wheels to PyPI
    needs: build-wheels
    runs-on: ubuntu-latest
    if: startsWith(github.ref, 'refs/tags/')
    steps:
      - name: Download all wheels
        uses: actions/download-artifact@v4
        with:
          path: dist
          merge-multiple: true

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install twine
        run: pip install --upgrade twine

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*.whl
```
The secrets were handled using the github secrets setting which was way secure rather than storing it in some repository file.
I did all of this in a virtual env. to avoid corrupting my existing project codebase due to the installation of various tools like `twine` etc.

### The execution

All of the plan was pretty much picture perfect, but the real pain came when I had to see multiple deployments fail due to errors in the `.yml` file ranging from syntax errors to constraint mismatches in build tool versions. It was brutal finding those errors and fixing them just to find something else breaking on the next deployment cycle.

I had to create 7 new versions just for the sake of checking whether something got pushed into pypi index in a single session. After a long tiresome session of finding dumb errors and tagging the versions, pushing them, and hoping the deployment succeeds, I got my first build wheel on the pypi index and it was an amazing feeling. Later, on the subsequent deployment cycles i got all of the build wheels.

### Testing 

The last stage was to test the pip install on a virtual env. to make sure nothing has broken and tool worked as it was intended to work.

