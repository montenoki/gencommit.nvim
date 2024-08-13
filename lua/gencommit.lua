local config = {}

local function setup(cfg)
	config = cfg
	-- add keymaps here
	vim.keymap.set("n", "<Leader>i", ":call ExPlugEcho()<CR>", { silent = true })
end

-- Used in Python to get config
local function getConfig()
	return config
end

return { setup = setup, getConfig = getConfig }
