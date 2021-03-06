# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
    _name = 'wechat_mall.category'
    _description = u'商品分类'
    _order = 'level,sort'

    name = fields.Char(string='名称', required=True)
    category_type = fields.Char(string='类型')
    pid = fields.Many2one('wechat_mall.category', string='上级分类', ondelete='cascade')
    child_ids = fields.One2many('wechat_mall.category', 'pid', string='子品类')
    key = fields.Char(string='编号')
    icon = fields.Many2one('ir.attachment', string='图标')
    level = fields.Integer(string='分类级别', compute='_compute_level')
    is_use = fields.Boolean(string='是否启用', default=True, required=True)
    sort = fields.Integer(string='排序')

    goods_ids = fields.One2many('wechat_mall.goods', 'category_id', '商品')

    @api.one
    @api.depends('pid')
    def _compute_level(self):
        level = 0
        pid = self.pid
        while True:
            if not pid:
                break

            pid = pid.pid

            level += 1

        self.level = level
