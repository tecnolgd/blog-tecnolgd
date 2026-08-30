[← Home](../index.md)

## From Local Builds to `pip install`: repoScanner v0.3.0-beta.9
*Aug 2026 | Category: tools/build*

> Source(s)
> PyPI: [https://pypi.org/project/repoScanner](https://pypi.org/project/repoScanner/)
> GitHub: [tecnolgd/repoScanner](https:github.com/tecnolgd/repoScanner)


I recently shipped the latest version of [repoScanner](https:github.com/tecnolgd/repoScanner), making it fully installable via `pip`. 

It turned out to be one of the most tedious release cycles I’ve worked on. The goal was to package prebuilt C++ binaries so users could run a simple `pip install repoScanner` and immediately get native performance without touching `gcc`, `make`, or local build dependencies. Watching it run seamlessly in a fresh environment made the trial-and-error completely worth it.

### The Motivation: Eliminating Setup Friction

When the core utility was working locally, it felt complete. However, expecting end-users to manually build native libraries from source is a massive adoption barrier. 

I wanted to bridge the gap between low-level performance and high-level developer experience. By wrapping the core C++ engine (`libcvault`) into a Python package, users get native execution speeds alongside single-command cross-platform installation.

### The Architecture: Automated Wheels with `cibuildwheel`

To deliver precompiled binaries across different operating systems, I set up a `cibuildwheel` pipeline paired with GitHub Actions:

- **Linux:** Build native binary wheels embedding the compiled C++ engine (`libcvault`).
- **macOS / Windows:** Fall back to native Python executables for broad environment compatibility(as of now).
- **Automated PyPI Publishing:** Trigger build and upload workflows exclusively on tagged releases.

Here is a snippet used for publishing artifacts to PyPI:

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

Using GitHub Secrets kept sensitive PyPI credentials out of the codebase, and working inside an isolated virtual environment prevented global package pollution during local testing.

### The Reality of CI/CD Debugging

The architecture looked clean and perfect as a plan, but pulling it off was brutal.    

Deployments failed repeatedly dude to issues ranging from yml/yaml syntax errors, dependency version inconsistency to missing wheel targets. Fixing one error often surfaced another somewhere else. I ended up tagging ~7 test releases in a single session just to debug the pipeline and verify artifacts on PyPI. Getting that first green checkmark and seeing the compiled .whl files hit the index was a huge win.

### Testing & Future

To verify the release, I spun up a clean virtual environment to test installation and execution:

```bash
python3 -m venv test_env 
source test_env/bin/activate
pip install repoScanner
```

The Good part: Everything executed as expected with zero manual configuration required. Solving packaging friction is tedious work, but automating it once pays off for every release that follows.   

Now I have taken a break from heavy project work and next i would be looking forward to make the tool efficient and maybe add additional features and native wheel options for windows and mac os environments. Thanks to the contributors of the `repoScanner` and users, if any.

