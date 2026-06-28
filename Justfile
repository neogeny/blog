alias p := preview
alias b := build
alias s := serve

output := "build/html"
config := "pelicanconf.py"

port := "8000"

# Build site (development)
build:
    uv run pelican -s {{config}}

# Remove generated files
clean:
    rm -rf {{output}}
    mkdir -p {{output}}

# Build with full regeneration
rebuild:
    uv run pelican -d -s {{config}}

# Auto-regenerate on file changes
regenerate:
    uv run pelican -r -s {{config}}

# Serve build output at http://localhost:{{port}}
serve:
    uv run pelican -l {{output}} -s {{config}} -p {{port}}

# Build then serve
reserve: build serve

# Build with production settings (same as build, both use pelicanconf.py)
preview: build

# Publish to GitHub Pages via ghp-import
ghp: build
    uv run ghp-import -n -p -f {{output}}

# Show available targets
default:
    @just --list
